package programasPoo;

//clase bicicleta, hereda de vehiculo
public class Bicicleta extends Vehiculo{ 
	
	private int pinones; // numero de piñones
	
	//constructor
	public Bicicleta(int p){
		super(); //llamo al constructor de la clase padre abstracta(vehiculo)
		this.pinones=p;
	}
	
	/**metodo vacio.
	 * 
	 * hace un caballito la bicicleta
	 * 
	 * */
	public void hazCaballito() {
    System.out.println("Estoy haciendo el caballito");
	} 
}
