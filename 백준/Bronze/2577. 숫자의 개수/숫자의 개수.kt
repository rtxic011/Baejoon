fun main() {
    var a = mutableListOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    var q = readLine()!!.toInt()
    for (i in 1..2) {
        q *= readLine()!!.toInt()
    }
    for (i in q.toString() ) {
        val ch = i - '0'
        a[ch] += 1
    }
    for ( i in 0..9 ) {
        println(a[i])
    }
}