// Classes

class User {
    constructor(name, surname, phone, email, gender) {
        this.name = name;
        this.surname = surname;
        this.phone = phone;
        this.email = email;
        this.gender = gender;
    }
}


class Card {
    constructor(number, holder, expMonth, expYear, cvv, balance) {
        this.number = number;
        this.holder = holder;
        this.expMonth = expMonth;
        this.expYear = expYear;
        this.cvv = cvv;
        this.balance = balance;
    }

    toHtml() {
        return `<div class="card-small">
                   <img src="/uploads/2022/11/card-bg.png">
                   <p>${this.number}</p>
                   <p>${this.holder.name} ${this.holder.surname}</p>
                   <p>${this.expMonth}/${this.expYear}</p>
                   <div class="cvv">${this.cvv}</div>
               </div>`;
    }

}

// Elements
let cardNumber = document.querySelector('.card-number');
let cardExpireMonth = document.querySelector('.card-expire-month');
let cardExpireYear = document.querySelector('.card-expire-year');
let cardHolderName = document.querySelector('.card-holder-name');
let cardHolderSurname = document.querySelector('.card-holder-surname');
let cardHolderPhone = document.querySelector('.card-holder-phone');
let cardHolderEmail = document.querySelector('.card-holder-email');
let cardHolderGender = document.querySelector('.card-holder-gender');
let cardListField = document.querySelector('.cards');
let createCardBtn = document.querySelector('.create-card-btn');

// Variables globales
let cvv = 100;
const cards = [];

// Events
createCardBtn.addEventListener('click', () => {
    const userFields = [
        cardHolderName,
        cardHolderSurname,
        cardHolderPhone,
        cardHolderEmail,
        cardHolderGender
    ];

    let isValid = true;

    for (const field of userFields) {
        if (field.value === '') {
            isValid = false;
            break;
        }
    }

    if (!isValid) {
        alert('Rellena todos los campos con informacion!');
    } else {
        let holder = new User(
            cardHolderName.value,
            cardHolderSurname.value,
            cardHolderPhone.value,
            cardHolderEmail.value,
            cardHolderGender.value
        );

        let card = new Card(
            cardNumber.value,
            holder,
            cardExpireMonth.value,
            cardExpireYear.value,
            cvv,
            1000
        );

        cvv += 1;
        cards.push(card);
        cardListField.innerHTML += card.toHtml();
    }
});
