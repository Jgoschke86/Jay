#include <Python.h>

static PyObject *
john_system(PyObject *self, PyObject *args) {
    const char *cmd;
    int sts;
    /* parse args */
    if (!PyArg_ParseTuple(args, "s", &cmd))
        return NULL;

    /* interface with the outside world */
    sts = system(cmd);

    /* return something */
    return PyLong_FromLong(sts);
}

static PyObject *
john_add(PyObject *self,PyObject *args) {
    int x,y,sum;

    if (!PyArg_ParseTuple(args, "ii", &x, &y))
        return NULL;
    sum = x + y;
    return PyLong_FromLong(sum);
}

static PyMethodDef johnMethods[] = {
    {"system",  john_system, METH_VARARGS, "Execute a shell command."},
    {"add",  john_add, METH_VARARGS,"add two integers"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef johnmodule = {
    PyModuleDef_HEAD_INIT,
    "john",
    NULL,
    -1,
    johnMethods
};

PyMODINIT_FUNC
PyInit_john(void) {
    return PyModule_Create(&johnmodule);
}
