#define PY_SSIZE_T_CLEAN
#include <Python.h>

static int
list_realloc(PyListObject *self, Py_ssize_t newsize) {
    PyObject **items;
    size_t num_allocated_bytes;
    if (newsize <= 0) {
        PyMem_FREE(self->ob_item);
        self->ob_item = NULL;
        self->allocated = 0;
        return 0;
    }

    if (newsize > PY_SSIZE_T_MAX / (Py_ssize_t)sizeof(PyObject *)) {
        PyErr_NoMemory();
        return -1;
    }

    num_allocated_bytes = (size_t)newsize * sizeof(PyObject *);
    items = (PyObject **)PyMem_Realloc(self->ob_item, num_allocated_bytes);
    if (items == NULL) {
        PyErr_NoMemory();
        return -1;
    }
    self->ob_item = items;
    self->allocated = newsize;
    return 0;
}

static int
list_shrink_to_fit_impl(PyListObject *self) {
    Py_ssize_t size = PyList_GET_SIZE(self);
    if (size == self->allocated)
        return 0;
    return list_realloc(self, size);
}

static int
list_reserve_impl(PyListObject *self, Py_ssize_t newsize) {
    Py_ssize_t allocated = self->allocated;
    if (allocated >= newsize)
        return 0;
    return list_realloc(self, newsize);
}

static PyObject *
list_shrink_to_fit(PyObject *self, PyObject *args) {
    PyObject *o;

    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'shrink_to_fit' expected list object.");
        return NULL;
    }
    PyListObject *list = (PyListObject *)o;
    if (list_shrink_to_fit_impl(list) < 0) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject *
list_reserve(PyObject *self, PyObject *args) {
    Py_ssize_t size;
    PyObject *o;

    if (!PyArg_ParseTuple(args, "On", &o, &size)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'reserve' expected list object.");
        return NULL;
    }
    PyListObject *list = (PyListObject *)o;
    if (list_reserve_impl(list, size) < 0) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject *
list_capacity(PyObject *self, PyObject *args) {
    PyObject *o;
    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'capacity' expected list object.");
        return NULL;
    }
    PyListObject *list = (PyListObject *)o;
    Py_ssize_t allocated = list->allocated;
    PyObject *capacity = PyLong_FromSsize_t(allocated);
    if (capacity == NULL) {
        return NULL;
    }
    return capacity;
}

static PyObject *
list_allocated_bytes(PyObject *self, PyObject *args) {
    PyObject *o;
    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'allocated_bytes' expected list object.");
        return NULL;
    }
    PyListObject *list = (PyListObject *)o;
    Py_ssize_t allocated_bytes = list->allocated * sizeof(PyObject *);
    PyObject *capacity = PyLong_FromSsize_t(allocated_bytes);
    if (capacity == NULL) {
        return NULL;
    }
    return capacity;
}

static PyObject *
list_stats(PyObject *self, PyObject *args) {
    PyObject *o;
    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'stats' expected list object.");
        return NULL;
    }
    PyListObject *list = (PyListObject *)o;
    Py_ssize_t length = PyList_GET_SIZE(list);
    Py_ssize_t allocated = list->allocated;
    Py_ssize_t allocated_bytes = allocated * sizeof(PyObject *);
    Py_ssize_t overhead = allocated - length;
    // capacity == 0 would divide by zero; report 0.0 utilization instead.
    double utilization = allocated == 0 ? 0.0 : (double)length / (double)allocated;

    PyObject *dict = PyDict_New();
    if (dict == NULL) {
        return NULL;
    }

    PyObject *values[5] = {
        PyLong_FromSsize_t(length),          PyLong_FromSsize_t(allocated),
        PyLong_FromSsize_t(allocated_bytes), PyLong_FromSsize_t(overhead),
        PyFloat_FromDouble(utilization),
    };
    const char *keys[5] = {
        "length", "capacity", "allocated_bytes", "overhead", "utilization",
    };
    for (int i = 0; i < 5; i++) {
        if (values[i] == NULL) {
            for (int j = 0; j < 5; j++) {
                Py_XDECREF(values[j]);
            }
            Py_DECREF(dict);
            return NULL;
        }
    }
    for (int i = 0; i < 5; i++) {
        if (PyDict_SetItemString(dict, keys[i], values[i]) < 0) {
            for (int j = i; j < 5; j++) {
                Py_DECREF(values[j]);
            }
            Py_DECREF(dict);
            return NULL;
        }
        // SetItemString INCREFs the stored value; release our own reference.
        Py_DECREF(values[i]);
    }
    return dict;
}

static PyMethodDef methods[] = {
    {"reserve", list_reserve, METH_VARARGS, "Reserve list capacity."},
    {"capacity", list_capacity, METH_VARARGS, "Return list capacity."},
    {"allocated_bytes", list_allocated_bytes, METH_VARARGS,
     "Return list allocated memory size."},
    {"shrink_to_fit", list_shrink_to_fit, METH_VARARGS, "Shrink to fit list capacity."},
    {"stats", list_stats, METH_VARARGS, "Return list memory statistics as a dict."},
    {NULL}};

// module definition struct
static struct PyModuleDef module = {PyModuleDef_HEAD_INIT, "list_reserve",
                                    "list memory allocation library", -1, methods};

// Initializes module
PyMODINIT_FUNC
PyInit_list_reserve(void) {
    return PyModule_Create(&module);
}
