package programasPoo;

public class PruebaTerminal {

  public static void main(String[] args) {
    //instancias 
    Terminal t1=new Terminal("663654985");
    Terminal t2=new Terminal("678456598");
    Terminal t3=new Terminal("636658247");
    
    System.out.println(t1);
    System.out.println(t2);
    
    t1.llama(t2, 200);
    t2.llama(t3, 250);
    t1.llama(t3, 150);
    
    System.out.println(t1);
    System.out.println(t2);
    System.out.println(t3);
  
    
  }

}
