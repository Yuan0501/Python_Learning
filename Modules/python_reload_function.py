import importlib
import sample_reload
# sample_reload modules has been imported more than once
importlib.reload(sample_reload)
importlib.reload(sample_reload)
importlib.reload(sample_reload)

# reload function can make dynamic changes within your code with import statements
import filechanges
def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit enter to reload...")