class Nodes <T> {
    T data;                   //Making the data portion and
    Nodes next;               //Same class's reference

    Nodes(){                  //Inside the constructer
        this.data = null;     //Make the data(Should not be null) to null
        this.next = null;     //and next to null(Should be null)
    }

}

public class MyList <T>{

    Nodes<T> head;                           //Initialize the head node to point other nodes.

    MyList(){
        this.head = new Nodes<T>();          //Implimenting the head node.   
    }

    public void add(T number) {             
        Nodes newNode = new Nodes();         //When the values are added to the linked list, 
        newNode.data = number;               //every time make a new node and put the value to the data.
        newNode.next = head.next;            //Now the address of the head is assigning to the new Node's reference.
        head.next = newNode;                 //Therefore previous node's address is belong to new node.
    }                                        //Then head can be refer the new node.
    
    public boolean isEmpty(){                //If head's reference is null, return 'null'
        return head.next == null;
    }
    
    public boolean hasElements(){          
        return head.next != null;             //If head's reference is not null, return nothing
    }
    public T remove(){
        T returnValue;                        //To remove value, first consider the above method, "isEmpty"
        if (!this.isEmpty()) {                //If it is not, 
             returnValue = (T)head.next.data; //head.next.data assign to the variable
            head.next = head.next.next;       //Neglect the first node and assign the reference of the next node by head node
        }
        else{
            returnValue = null;               //If the list is empty, return 'null'
        }
        return returnValue;                   //else the variable shoul be the removed data
    }
}
