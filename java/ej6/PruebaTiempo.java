package programasPoo;

public class PruebaTiempo {

	public static void main(String[] args) {
		Tiempo intervalo=new Tiempo(1,0,0);
		Tiempo intervalo2=new Tiempo(3,50,35);
		Tiempo intervalo3=new Tiempo(1,50,0);
		
		intervalo.suma(intervalo2);
		System.out.println(intervalo);
		intervalo.resta(intervalo3);
		System.out.println(intervalo);
		
		
	}
}
