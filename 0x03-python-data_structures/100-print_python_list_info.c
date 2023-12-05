#include <Python.h>
/**
 * print_python_list_info - prints info about a python list
 * @p: pointer to the python list
 * Return: returns nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *element_object_cast;
	const char *element_type;
	Py_ssize_t index, list_size;
	PyObject *element;

	element_object_cast = (PyListObject *)p;
	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", (int) list_size);
	printf("[*] Allocated = %d\n", (int)element_object_cast->allocated);

	for (index = 0; index < list_size; index++)
	{
		element = PyList_GetItem(p, index);
		element_type = Py_TYPE(element)->tp_name;
		printf("Element %d: %s\n", (int) index, element_type);
	}
}
