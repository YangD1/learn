<?php
    class LightSwitch {                         //  开关类

        public function on()                    // 开始
        {

        }

        public function off()                    // 关注
        {

        }

        protected function connect()                 // 连接
        {
            var_dump("connect");
        }

    }

    $light = new LightSwitch();
    $light -> connect();
