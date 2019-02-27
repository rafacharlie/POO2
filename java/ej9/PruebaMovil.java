package programasPoo;

public class PruebaMovil {

  public static void main(String[] args) {
    Movil m1= new Movil("663654985", "rata");
    Movil m2= new Movil("659863214", "bisonte");
    
    System.out.println(m1);
    System.out.println(m2);
    
    m1.llama(m2, 158);
    m2.llama(m1, 169);
    
    System.out.println(m1);
    System.out.println(m2);
    
  }
}
