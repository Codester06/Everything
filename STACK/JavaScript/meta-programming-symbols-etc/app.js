// Library land
const uid = Symbol();
console.log(uid);

const user = {
  // id: 'p1',
  [uid]: "p1",
  name: "Max",
  age: 30,
  [Symbol.toStringTag]: "User",
};

user[uid] = "p3";

// app land => Using the library

user.id = "p2"; // this should not be possible!

console.log(user[Symbol("uid")]);
console.log(Symbol("uid") === Symbol("uid"));
console.log(user.toString());

const company = {
  //   curEmployee: 0,
  employees: ["Max", "Manu", "Anna"],
  //   next() {
  //     if (this.curEmployee >= this.employees.length) {
  //       return { value: this.curEmployee, done: true };
  //     }
  //     const returnValue = {
  //       value: this.employees[this.curEmployee],
  //       done: false,
  //     };
  //     this.curEmployee++;
  //     return returnValue;
  //   },
  [Symbol.iterator]: function* employeeGenerator() {
    //     let employee = company.next();

    //     while(!employee.done) {
    //     yield employee.value;
    //     employee = company.next();
    // }
    let currentEmployee = 0;
    while (currentEmployee < this.employees.length) {
      yield this.employees[currentEmployee];
      currentEmployee++;
    }
  },
};

// let employee = company.next();

// while(!employee.done) {
//   console.log(employee.value);
//   employee = company.next();
// }

for (const employee of company) {
  console.log(employee);
}

console.log(...company);
// const it = company.getEmployee();
// console.log(it.next());
// console.log(it.next());
// console.log(it.next());
// console.log(it.next());
// console.log(it.next());

const person = ["person1", "person2"];
console.log(person);

const course = {
  title: "The CodeSter",
};
// reflect
Reflect.setPrototypeOf(course, {
  toString() {
    return this.title;
  },
});

console.log(course.toString())

// proxy

const courseHandler = {
  get(obj,propertyName){
    console.log(propertyName)
    if(propertyName === 'length'){
      return 0;
    }
    return obj[propertyName] || 'NOT FOUND';
  },

  set(obj,propertyName,value){
    if(propertyName === 'rating'){
      return ;
    }
    obj[propertyName] = value;
  }
}
const pCourse = new Proxy(course,courseHandler);
pCourse.rating = 5
console.log(pCourse.title ,pCourse.length,pCourse.rating)
// console.log(pCourse, course)