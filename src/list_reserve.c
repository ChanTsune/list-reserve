#define PY_SSIZE_T_CLEAN
#include <Python.h>


static int
_list_reserve(PyListObject *self, Py_ssize_t newsize)
{
    PyObject **items;
    size_t num_allocated_bytes;
    Py_ssize_t allocated = self->allocated;

    if (allocated >= newsize && newsize >= (allocated >> 1)) {
        assert(self->ob_item != NULL || newsize == 0);
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

static PyObject *
list_reserve(PyObject *self, PyObject* args) {
    Py_ssize_t size;
    PyObject* o;

    if (!PyArg_ParseTuple(args, "On", &o, &size)){
        return NULL;
    }
    if (!PyList_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "capacity excepted list object.");
        return NULL;
    }
    PyListObject* list = (PyListObject*)o;
    if (_list_reserve(list, size) < 0) {
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
        PyErr_SetString(PyExc_TypeError, "capacity excepted list object.");
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
    {"reserve", list_reserve, METH_VARARGS, "reserve list capacity"},
    {"capacity", list_capacity, METH_VARARGS, "return list capacity"},
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
