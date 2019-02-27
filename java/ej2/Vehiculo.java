package programasPoo;

public abstract class Vehiculo { //clase abstracta vehiculo
	
	//atributos de clase
	private static int kilometrosTotales=0;
	private static int vehiculosCreados=0;
	
	//atributos de instancia
	private int kilometrosRecorridos;
	
	//constructor
	public Vehiculo() {
		this.kilometrosRecorridos=0;
	}
	
	//metodos getter
	
	public int getKilometrosRecorridos() {
		return this.kilometrosRecorridos;
	}
	
	public static int getKilometrosTotales() {
		return Vehiculo.kilometrosTotales;
	}
	
	/**Metodo:
   * Hace que un vehículo recorra una distancia determinada.
   * 
   * Cuando un vehículo recorre una distancia k, se
   * incrementan su propio cuentakilómetros, es decir, su atributo
   * kilometrosRecorridos y también se incrementa la cuenta
   * global de kilómetros que recorren todos los vehículos, es decir, el
   * atributo de clase kilometrosTotales.
   *
   * @param k kilómetros a recorrer
   */
	
	public void recorre(k) {
		//variable de instancia
    this.kilometrosRecorridos += k;
    //variable de clase(static)
    Vehiculo.kilometrosTotales += k;
	}
}
