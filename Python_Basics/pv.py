import os
def date(): {

    os.system('date')
}

print("PV and PVC Creation")
print("-------------------\n")

print("Please enter project/namespace name")
ns = input()

print("Please enter PV name")
pv = input()


template = """apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {}
  namespace: {}
spec:
  storageClassName: “nfs” 
  volumeName: foo-pv"""

test = print(template.format(pv,ns))
#os.system("echo $test")
def main(): {
     date()
    
}

if __name__ == "__main__": 
    main()