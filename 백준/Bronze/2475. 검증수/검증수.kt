fun main() {
    val a = readLine()!!.split(" ").map { it.toInt() }
    var b = 0
    for (i in a) {
        b += i * i
    }
    b %= 10
    println(b)
}
