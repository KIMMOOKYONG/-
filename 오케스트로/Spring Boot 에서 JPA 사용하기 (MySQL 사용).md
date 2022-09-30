# 참조
- https://memostack.tistory.com/155

# MySQL 설정
## 1. MySQL 설치
- https://memostack.tistory.com/150

## 2. 데이터베이스 생성
- TEST_DB 생성
```sql
CREATE DATABASE TEST_DB 
DEFAULT CHARACTER SET UTF8;

```

## 3. 유저 생성 및 권한 부여
```sql
-- 사용자 생성
CREATE USER test_user@localhost
    IDENTIFIED BY 'admin';

-- DB 권한 부여
GRANT ALL PRIVILEGES
    ON TEST_DB.*
    TO test_user@localhost;

```

## 4. 테이블 생성
```sql
-- MEMBER 테이블 생성
CREATE TABLE IF NOT EXISTS TEST_DB.MEMBER (
    PID BIGINT NOT NULL AUTO_INCREMENT,
    USERNAME VARCHAR(200),
    NAME VARCHAR(200),
    PRIMARY KEY(PID)
);

```

# Spring Boot 예제
## 1. 의존성 추가
- spring-boot-starter-data-jpa
- mysql-connector-java
- 롬복 추가 (https://memostack.tistory.com/154)

## 2. Spring Boot와 MySQL 연동
```
server.address=localhost
server.port=8080

spring.datasource.url=jdbc:mysql://localhost:3306/TEST_DB?useSSL=false&characterEncoding=UTF-8&serverTimezone=UTC
spring.datasource.username=test_user
spring.datasource.password=admin
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# mysql 사용
spring.jpa.database=mysql
spring.jpa.database-platform=org.hibernate.dialect.MySQL5InnoDBDialect

# 로깅 레벨
logging.level.org.hibernate=info

# 하이버네이트가 실행한 모든 SQL문을 콘솔로 출력
spring.jpa.properties.hibernate.show_sql=true
# SQL문을 가독성 있게 표현
spring.jpa.properties.hibernate.format_sql=true
# 디버깅 정보 출력
spring.jpa.properties.hibernate.use_sql_comments=true

```

## 3. Entity 클래스 생성
```java
// MemberEntity
package com.example.demo.entity;

import lombok.*;

import javax.persistence.*;

@Getter // getter 메소드 생성
@Builder // 빌더를 사용할 수 있게 함
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity(name="member") // 테이블 명을 작성
public class MemberEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long pid;

    @Column(nullable = false, unique = true, length = 30)
    private String username;

    @Column(nullable = false, length = 100)
    private String name;

    public MemberEntity(String username, String name) {
        this.username = username;
        this.name = name;
    }
}

```

## 4. Repository 생성
```java
package com.example.demo.repo;

import com.example.demo.entity.MemberEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MemberRepository extends JpaRepository<MemberEntity, Long> {

}

```

## 5. Controller 생성
```java
package com.example.demo.controller;

import com.example.demo.entity.MemberEntity;
import com.example.demo.repo.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController // JSON 형태 결과값을 반환해줌 (@ResponseBody가 필요없음)
@RequiredArgsConstructor // final 객체를 Constructor Injection 해줌. (Autowired 역할)
@RequestMapping("/v1") // version1의 API
public class MemberController {

    private final MemberRepository memberRepository;

    /**
     * 멤버 조회
     * @return
     */
    @GetMapping("member")
    public List<MemberEntity> findAllMember() {
        return memberRepository.findAll();
    }

    /**
     * 회원가입
     * @return
     */
    @PostMapping("member")
    public MemberEntity signUp() {
        final MemberEntity member = MemberEntity.builder()
                .username("test_user@gmail.com")
                .name("test user")
                .build();
        return memberRepository.save(member);
    }
}

```

# 결과 확인
```
/v1/member 로 POST 방식으로 요청

```

```shell
$ curl -X POST http://localhost:8080/v1/member

```

```json
{"pid":1,"username":"test_user@gmail.com","name":"test user"}

```
