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

    num_allocated_bytes = newsize * sizeof(PyObject *);
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
list_shrink_to_fit(PyObject *self, PyObject* args) {
    PyObject* o;

    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'shrink_to_fit' expected list object.");
        return NULL;
    }
    PyListObject* list = (PyListObject*)o;
    if (list_shrink_to_fit_impl(list) < 0) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject *
list_reserve(PyObject *self, PyObject* args) {
    Py_ssize_t size;
    PyObject* o;

    if (!PyArg_ParseTuple(args, "On", &o, &size)){
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'reserve' excepted list object.");
        return NULL;
    }
    PyListObject* list = (PyListObject*)o;
    if (list_reserve_impl(list, size) < 0) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject *
list_capacity(PyObject *self, PyObject *args) {
    PyObject* o;
    if (!PyArg_ParseTuple(args, "O", &o)){
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "'capacity' expected list object.");
        return NULL;
    }
    PyListObject* list = (PyListObject*)o;
    long allocated = list->allocated;
    PyObject* capacity = PyLong_FromLong(allocated);
    if (capacity == NULL) {
        return NULL;
    }
    return capacity;
}


static PyMethodDef methods[] = {
    {"reserve", list_reserve, METH_VARARGS, "Reserve list capacity."},
    {"capacity", list_capacity, METH_VARARGS, "Return list capacity."},
    {"shrink_to_fit", list_shrink_to_fit, METH_VARARGS, "Shrink to fit list capacity."},
    {NULL}};

// module definition struct
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "list_reserve",
    "list memory allocation library",
    -1,
    methods};

// Initializes module
PyMODINIT_FUNC PyInit_list_reserve(void)
{
    return PyModule_Create(&module);
}
