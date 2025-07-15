fun main() {
    val (a, b) = readLine()!!.split(' ').map{ it.toInt()}
    if (a > b) {
        println(">")
    } else if (a < b) {
        println("<")
    } else {
        println("==")
    }
}