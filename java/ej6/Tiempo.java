package programasPoo;

public class Tiempo { //clase tiempo
	
	//atributos de instancia
	private int hora;
	private int min;
	private int seg;
	
	//constructor
	public Tiempo(int hora,int min,int seg) {
		this.hora=hora;
		this.min=min;
		this.seg=seg;
	}
		
	/**Metodo que suma
	 * 
	 * @param: objeto 
	 * @return: objeto
	 * */
	
	public Tiempo suma(Tiempo t) {
		hora= this.hora+t.hora;
		min=this.min+t.min;
		seg=this.seg+t.seg;
		
		if(min>=60) {
			hora+=1;
			min-=60;
		}
		if(seg>=60) {
			min+=1;
			seg-=60;
		}
		
		return new Tiempo(hora,min,seg);
	}

	@Override
	public String toString() {
		return "Tiempo [hora=" + hora + ", min=" + min + ", seg=" + seg + "]";
	}
	
	
	/**Metodo que resta
	 * 
	 * @param: objeto 
	 * @return: objeto
	 * */
	public Tiempo resta(Tiempo t) {
		//while(hora>=0 || min>=0 || seg>=0) {
		hora= this.hora-t.hora;
		min=this.min-t.min;
		seg=this.seg-t.seg;
		
		if(min>=60) {
			hora+=1;
			min-=60;
		}
		if(seg>=60) {
			min+=1;
			seg-=60;
		}
		//}
		return new Tiempo(hora,min,seg);
		
	}
}