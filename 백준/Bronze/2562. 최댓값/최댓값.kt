fun main() {
    val a = mutableListOf<Int>()
    for (i in 1..9) {
        a.add(readLine()!!.toInt())
    }
    val b = a.maxOrNull()
    println(b)
    println(a.indexOf(b)+1)
}