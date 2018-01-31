import VebTree form VEBTree
def main():
    print("the tree is empty  enter the size of the universe you want")
    print("HINT: size should be 2^(2^k)")
    k=int(input())
    v=VebTree(k)
    print("Enter the no of elemnts you want to add")
    n=int(input())
    for i in range(n):
        v.Insert(v.root,int(input()))
    f='Y'
    while y=='Y':
        print("Choose your option")
        print("1.Delete a element")
        print("2.Find predessor")
        print("3.FInd successor")
        print("4.Search a value in tree")
        print("5.Find the min")
        print("6.Find the max")
        x = int(input())
        if x==1:
            print("Enter a element to delete")
            s=int(input())
            v.Delete(v.root,s)
            print("you want to continue Enter Yes or N")
            sr=input()
            y=sr
        elif x==2:
            print("Enter a value to find its predessor")
            s=int(input())
            v.Predessor(v.root,s)
            print("You want to continue pess Y or N")
            sr=input()
            y=sr
        elif x==3:
            print("Enter a value to find its successor")
            s = int(input())
            v.Successor(v.root, s)
            print("You want to continue pess Y or N")
            sr = input()
            y = sr
        elif x==4:
            print("Enter a value to search in tree")
            s=int(input())
            v.Search(v.root,s)
            print("You want to Continue press Y or N")
            sr=input()
            y=sr
        elif x==5:
            print("the minimum in the tree is :")
            print(v.Minimum(v.root))
            print("You want to Continue press Y or N")
            sr = input()
            y = sr
        elif x==6:
            print("the maximum in the tree is :")
            print(v.Maximum(v.root))
            print("You want to Continue press Y or N")
            sr = input()
            y = sr
        else:
            print("Invalid choice input again")
            y="Y"
if __name__ =="__main__":
    main()
