object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
    println("Max value = " + if_method(15,21))
    for_method(Array(2,5,8,5,9,10,12))
  }

  def if_method(x:Int, y:Int ) : Int = {
	val maximo = if (x > y) x else y
	return maximo
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