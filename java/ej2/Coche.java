package programasPoo;

public class Coche extends Vehiculo{
	//atributo de instancia
	private int cilindrada; //cilindrada en cm3
	
	public Coche(int c) { //constructor
		super(); //llamo al constructor de la clase padre abstracta(vehiculo)
		this.cilindrada=c;
	}
	
	/**metodo vacio.
	 * 
	 * Quema la rueda del coche
	 * 
	 * */
	public void quemaRueda() {
		System.out.println("Fffshhhhhhhhhhh");
	}
	
}
