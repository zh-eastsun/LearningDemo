package com.zdy.kotlin.demo.coroutine

import kotlinx.coroutines.*

// 协程的关键参数
val job = Job()                     // 没有返回值的任务，有返回值的任务：Deferred<ReturnType>
val dispatcher = Dispatchers.IO     // 协程分发器，标识当前协程作用域所处的线程
val scope = CoroutineScope(job + dispatcher)    // 协程作用域，可以理解为协程的生命周期，可以控制其内部的所有任务

suspend fun main() {
    // 创建协程的函数
    // runBlocking会阻塞当前线程的运行，直到当前协程运行完后才会执行后面的代码
    val result = runBlocking(job + dispatcher) {
        println("【协程】runBlocking 创建的协程")
        "runBlocking返回值"
    }
    // 哪怕上述代码是IO线程的，但是仍会阻塞到后续代码
    println("【主线程】runBlocking after")
    println("【主线程】runBlocking 返回值为: $result")

    // launch是最常见的启动协程方式，默认是由上下文决定所处线程
    // 不会阻塞当前线程
    // 返回值为一个job
    val job = scope.launch {
        println("【协程】launch 创建的协程")
    }
    // 没有阻塞主线程，有可能先执行以下代码
    println("【主线程】launch after")
    // 等待当前任务执行完毕，可以发现Job类型的任务是没有返回值的
    println("【主线程】launch 返回值为：${job.join()}")
}