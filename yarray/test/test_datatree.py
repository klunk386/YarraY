from datatree import Database, Trace
import numpy as np

if 0:
    DB = Database('My Project')
    DB.add_child('Group 1')
    DB.get_child('Group 1').add_child('Trace 1','data',np.random.randn(5000,5000))
    DB.get_child('Group 1').add_child('Trace 2','data',np.random.randn(5000,5000))
    DB.get_child('Group 1').add_child('Trace 3','data',np.random.randn(5000,5000))
    DB.add_child('Group 2')
    DB.get_child('Group 2').add_child('Trace 4','data',np.random.randn(5000,5000))
    DB.get_child('Group 2').add_child('Trace 5','data',np.random.randn(5000,5000))
    DB.get_child('Group 2').add_child('Trace 6','data',np.random.randn(5000,5000))

if 0:
    DB = Database('My Project')
    DB.add_child('Group 1')
    DB.get_child('Group 1').add_child('Trace 1','data',data=Trace())
    DB.get_child('Group 1').get_child('Trace 1').data.data=np.random.randn(5000,5000)
    DB.get_child('Group 1').get_child('Trace 1').get_path()
    DB.del_child('Group 1')


if 1:
    DB = Database('My Project')
    C1 = DB.add_child('Group 1')
    C2 = C1.add_child('Trace 1')
    C2.data = Trace()
    C2.data.data = np.random.randn(5000,5000)
    del C1
    del C2
    DB.del_child('Group 1')
