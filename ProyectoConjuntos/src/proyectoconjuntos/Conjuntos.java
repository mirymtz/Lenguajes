package proyectoconjuntos;

import java.util.Scanner;


public class Conjuntos {
    
    
    public void leer(){
        Scanner leer = new Scanner(System.in);
        System.out.println("Introduce el Numero de elementos de A");
        int ca = leer.nextInt();
        System.out.println("Introduce el Numero de elementos de B");
        int cb = leer.nextInt();
        
        int[]a=new int[ca];
        int[]b=new int[cb];
        
        System.out.println("Introduce los elementos de A");
        for (int i = 0; i <a.length; i++) {
            a[i]=leer.nextInt();
        }
        
        System.out.println("Introduce los elementos de B");
        for (int i = 0; i <b.length; i++) {
            b[i]=leer.nextInt();
        }
        
        int[]U=Union(a,b);
        int[]I= Interseccion(a,b);
        
        System.out.println("Los Elementos de la Union Son: ");
        for (int i = 0; i < U.length; i++) {
            System.out.println(U[i]); 
        }
        
        System.out.println("Los elementos de Interseccion Son: ");
        for (int i = 0; i < I.length; i++) {
            System.out.println(I[i]);
        }
    }
    
        
    
    public static Boolean existe(int[] conjunto, int elemento){
       Boolean existe = false;
       for(int i=0;  i < conjunto.length; i++){
           if(conjunto[i]==elemento){
               existe=true;
           }
           
       }
       
       return existe;
              
        
    }
    
    public static int[] Union(int[]a,int[]b){
        
        int[]U= new int[a.length+b.length];
        for (int i = 0; i < a.length; i++) {
            U[i]=a[i];
        }
        
        int x=0;
        int r=0;
        for (int i = 0; i < b.length; i++) {
            if(existe(U, b[i])==false){
                U[a.length+x]=b[i];
                x++;
            }
            else{
                r++;  
            }
        
        }
        int[] auxiliar=U;
        U=new int[auxiliar.length-r];
        
        for (int i = 0; i < U.length; i++) {
            U[i]=auxiliar[i];
        }
        
        return U;
          
    }

    public static int[]Interseccion(int[]a, int[]b){
        int c=0;
        for (int i = 0; i < a.length; i++) {
            if(existe(b,a[i])){
                c++;
            }
            
        }
        int[]I=new int[c];
        int x=0;
        
        for (int i = 0; i < a.length; i++) {
            if(existe(b,a[i])){
                I[x]=a[i];
                x++;
            }
        }
        return I;
    }
}
