# 참조
- https://youbiiin.tistory.com/12

# Vue.js를 사용하여 Todo List 만들기
```
Vue.js를 이용하여 Todo List를 만들어 볼 예정이다.
상태관리는 Vuex를 사용하며, localStorage에 데이터를 저장해보려한다.

```

# 화면설계
```
1) 오늘 날짜 노출
2) 리스트 총 개수와 리스트 완료여부 개수 나타남
3) 인풋
4) 인풋에 텍스트 입력 후 등록 버튼 누르면 리스트 추가
5) 최신순, 오래된 순에 따라 리스트 필터링
6) 전체삭제 버튼을 누르면 리스트 전체 삭제
7) 체크박스 클릭 시 완료된 리스트
8) 등록한 날짜 노출
9) 한개의 리스트 삭제

```

![image](https://user-images.githubusercontent.com/102650331/190868134-f9aacd43-34a1-41ad-a45a-644528c297e2.png)

# 폴더구조
![image](https://user-images.githubusercontent.com/102650331/190868613-dca52c5a-d6e8-42d2-8cd8-26120dfa2391.png)

![image](https://user-images.githubusercontent.com/102650331/190868628-aba4c3c1-85a8-4cc3-9c4a-bbd2437708c1.png)

## layouts/index.vue
![image](https://user-images.githubusercontent.com/102650331/190868682-1853146c-37ec-4a3a-b997-f0666a9150d3.png)

```html
<template>
    <div>
        <todo-header></todo-header>
        <slot></slot> <!-- 여기에 컨텐츠 영역이 들어감. -->
        <todo-footer></todo-footer>
    </div>
</template>
 
<script>
import TodoHeader from './TodoHeader.vue'
import TodoFooter from './TodoFooter.vue'
 
export default {
    components: { TodoHeader, TodoFooter },
 
}
</script>


```

