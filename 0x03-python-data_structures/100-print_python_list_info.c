#include <Python.h>

void print_python_list_info(PyObject *p){
    if(p == NULL)
        return;
    if(PyList_Check(p))
        printf("List\n");
    else if(PyTuple_Check(p))
        printf("Tuple\n");
    else if(PyDict_Check(p))
        printf("Dict\n");
    else if(PySet_Check(p))
        printf("Set\n");
    else if(PyFrozenSet_Check(p))
        printf("FrozenSet\n");
    else if(PyLong_Check(p))
        printf("Integer\n");
    else if(PyFloat_Check(p))
        printf("Float\n");
    else if(PyUnicode_Check(p))
        printf("String\n");
}
