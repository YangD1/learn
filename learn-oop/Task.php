<?php
    class Task{
        public $description ;
        public $completed = false;

        public function __construct($description)
        {
            $this->description = $description;
        }

        public function complete()
        {
            $this-> completed = true;
        }

    }

    $task = new Task("im YoungDee");
    $task2 = new Task("im PHP OOP");
    // $task -> complete();
    var_dump($task->description);
    var_dump($task2->description);
