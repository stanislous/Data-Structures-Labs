public class Main {
    public static void main(String argc[]){
        MyList myList = new MyList();
        myList.isEmpty();
        myList.add(2135);
        System.out.println("Values are added.");
        myList.add("H");
        myList.add(234);
        System.out.println("Remove elements.");
        System.out.println("Remove an element: "+myList.remove());
        System.out.println("Remove an element: "+myList.remove());
        System.out.println("Remove an element: "+myList.remove());
        System.out.println("Remove an element: "+myList.remove());
        System.out.println("Is the list empty? "+myList.isEmpty());
        System.out.println("Are there any element in linked list? "+myList.hasElements());
        System.out.println("Values are added.");
        myList.add("Shehan");
        myList.add("e13377");
        System.out.println("Remove elements.");
        System.out.println("Are there any element in linked list? "+myList.hasElements());
        System.out.println("Remove an element: "+myList.remove());
        System.out.println("Remove an element: "+myList.remove());
    }
}
