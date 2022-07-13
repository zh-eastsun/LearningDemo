plugins {
    java
    kotlin("jvm") version "1.5.0"
}

group = "com.zdy.kotlin.demo"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.4.3")
    testImplementation("junit", "junit", "4.12")
}
