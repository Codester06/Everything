const customer = ['codester','vivek','codexter']

const activeCustomer = ['codester','vivek']
const inactiveCustomer = _.difference(customer, activeCustomer)
console.log(inactiveCustomer) // lodash 