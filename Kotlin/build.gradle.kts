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
    testImplementation("junit", "junit", "4.12")
}
