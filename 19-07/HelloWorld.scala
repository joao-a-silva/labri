object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
    println("Max value = " + if_method(15,21))
  }

  def if_method(x:Int, y:Int ) : Int = {
	val maximo = if (x > y) x else y
	return maximo
  }
}