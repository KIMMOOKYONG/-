# GET API 만들기
![image](https://user-images.githubusercontent.com/102650331/191974668-0458a21b-592b-433c-bff1-19cbb9e68b75.png)

![image](https://user-images.githubusercontent.com/102650331/191974748-1a1e1b63-e344-4bff-8d46-42093e4e8b70.png)

# @RequestMapping으로 구현하기

```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @RequestMapping(value = "/hello", method = RequestMethod.GET)
    public String getHello() {
        return "Hello World";
    }
}


```

![image](https://user-images.githubusercontent.com/102650331/191976042-891ff4a7-fb90-46eb-83ce-2aaad4385877.png)

# 매개변수가 없는 GET 메서드 구현

```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/name")
    public String getName() {
        return "Flature";
    }
}


```

![image](https://user-images.githubusercontent.com/102650331/191976831-48702479-3c84-49b0-85fc-807b5734916b.png)


# @PathVariable을 활용한 GET 메서드 구현

```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/variable1/{variable}")
    public String getVariable1(@PathVariable String variable) {
        return variable;
    }
}


```

![image](https://user-images.githubusercontent.com/102650331/191980617-6f6799ca-47e5-4c4e-b369-959151c82e0a.png)

```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/variable2/{variable}")
    public String getVariable2(@PathVariable("variable") String var) {
        return var;
    }
}


```

![image](https://user-images.githubusercontent.com/102650331/191981210-75568a91-ecfc-406d-b6fb-6dbeb0109d23.png)
