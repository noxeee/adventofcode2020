import scala.io.Source

object Day8 {
    
    def parse(input:String): (String, Int) = {
        val inputs = input.split(" ")
        var operation:String = inputs(0)
        var number:Int = inputs(1).toInt
        println("Op: " + operation + " Num: " + number)
        (operation, number)
    }

    def visitedTwice(visited:scala.collection.mutable.Map[String, Int]): Boolean = {
        visited.values.exists(_ == 2)
    }

    def checkVisitedStatus(op:String, visited:scala.collection.mutable.Map[String, Int]): Boolean = {
        if (!visited.contains(op)) { 
            visited += (op -> 1)
            println(visited)
            visitedTwice(visited)
        }
        else { 
            visited.update(op, visited(op)+1)
            println(visited)
            visitedTwice(visited)
        }
    }


    def findLoop(input:Array[String]){
    
        val visited = scala.collection.mutable.Map[String, Int]()
        var acc:Int = 0
        var idx:Int = 0

        while (!visitedTwice(visited)) {
            
            val (op, num) = parse(input(idx))
            println("Op: " + op + "Num" + num)
            //val inputs = parse(input(idx))

            op match {
                case "nop" => 
                    val check = checkVisitedStatus(op, visited)
                    if (check) {
                        println(acc)
                    }
                case "acc" => 
                    val check = checkVisitedStatus(op, visited)
                    if (check) {
                        println(acc)
                    }
                    acc += num 

                case "jmp" => 
                    val check = checkVisitedStatus(op, visited)
                    if (check) {
                        println(acc)
                    }
                    idx += num

                case _ => println("This shouldn't happen?")
            }
            idx += 1
        }
        println(acc)
    }

    def main(args: Array[String]): Unit = {
            // reading file in Scala
        //val filename = "input_day8.txt"
        val filename = "example.txt"
        val lines = Source.fromFile(filename).getLines.toArray
        println(lines)
        println(findLoop(lines))        
    }

}