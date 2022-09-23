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


