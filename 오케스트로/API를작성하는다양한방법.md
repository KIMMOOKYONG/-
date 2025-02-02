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

# @RequestParam을 활용한 GET 메서드 구현

```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/request1")
    public String getRequestParam1(
            @RequestParam String name,
            @RequestParam String email,
            @RequestParam String organization
    ) {
        return  name + " " + email + " " + organization;
    }
}



```

![image](https://user-images.githubusercontent.com/102650331/191982568-259229b2-b80f-4f6b-aca4-46a901544274.png)


```java
package com.spring.api.controller;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/request2")
    public String getRequestParam2(@RequestParam Map<String, String> param) {
        StringBuilder sb = new StringBuilder();
        param.entrySet().forEach(map -> {
            sb.append(map.getKey() + " : " + map.getValue() + "\n");
        });
        return sb.toString();
    }
}



```

![image](https://user-images.githubusercontent.com/102650331/191983928-b2515f51-d51c-4b6c-8839-3277a6471348.png)


# DTO 객체를 활용한 GET 메서드 구현
![image](https://user-images.githubusercontent.com/102650331/191984425-ab280fcb-e71e-4cd4-8ca2-e9c4535afc0b.png)

```java
package com.spring.api.controller;

import com.spring.api.dto.MemberDto;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    @GetMapping(value = "/request3")
    public String getRequestParam3(MemberDto memberDto) {
        return memberDto.toString();
    }
}


```

![image](https://user-images.githubusercontent.com/102650331/191986846-7aef3eb3-3e0b-4b97-a039-cde6eaec0038.png)

