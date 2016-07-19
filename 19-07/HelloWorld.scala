class Calculatrice(val x:Int, val y:Int){
	def soma(): Int ={
		//val result = x+y
		return x + y
	}

	def if_method() : Int = {
		val maximo = if (x > y) x else y
		return maximo
  	}



}


object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")

    for_method(Array(2,5,8,5,9,10,12))

    var calc = new Calculatrice(5,3)
    val result= calc.soma()
    println("Result soma= " + result)
        println("Max value = " + calc.if_method())
  }

  

  def for_method(lista: Array[Int]): Unit = {
    //val lista = lista(1, 2, 3, 4)
    // for loop execution with a range
    for( i <- 0 to 6){
      if (lista(i) % 2 == 0) {
      	println( lista(i) );
      }
    }
  }




}