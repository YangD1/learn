<?php

class Person {
    public $name;       // 类属性 姓名
    public $age;        // 类属性 年龄

    function __construct($name)
    {
        $this -> name = $name;
    }

    public function setAge($age){
        if( $age < 18 ){
            throw new Exception("not old enough");
            die();
        }
        $this -> age = $age;
    }

}
$youngdee = new Person("YoungDee");
$youngdee->age = 17;
var_dump($youngdee);
