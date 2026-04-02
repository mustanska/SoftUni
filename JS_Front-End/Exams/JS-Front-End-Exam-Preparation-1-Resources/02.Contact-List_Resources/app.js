window.addEventListener("load", solve);

function solve() {
    const nameInputElement = document.getElementById('name');
    const numberInputElement = document.getElementById('phone');
    const categoryElement = document.getElementById('category');

    const checkListElement = document.getElementById('check-list');
    const contactListElement = document.getElementById('contact-list');

    const addBtnElement = document.getElementById('add-btn');
    addBtnElement.addEventListener('click', addContactHandler);

    function addContactHandler(e) {
      const name = nameInputElement.value.trim();
      const phone = numberInputElement.value.trim();
      const category = categoryElement.value;

      if(!name || !phone || !category) {
        return;
      }

      const contactInfo = {name, phone, category};
      const contact = createContactElement(contactInfo);

      checkListElement.appendChild(contact);

      clearInputFields();
    }

    function createContactElement(contactInfo) {
      const liElement = document.createElement('li');
      const articleElement = document.createElement('article');
      const divButtonstElement = document.createElement('div');
      divButtonstElement.classList.add('buttons');
      
      const pNameElement = document.createElement('p');
      pNameElement.textContent = `name:${contactInfo.name}`;
      articleElement.appendChild(pNameElement);

      const pPhoneElement = document.createElement('p');
      pPhoneElement.textContent = `phone:${contactInfo.phone}`;
      articleElement.appendChild(pPhoneElement);

      const pCategoryElement = document.createElement('p');
      pCategoryElement.textContent = `category:${contactInfo.category}`;
      articleElement.appendChild(pCategoryElement);

      const editBtnElement = document.createElement('button');
      editBtnElement.classList.add('edit-btn');
      divButtonstElement.appendChild(editBtnElement);
      editBtnElement.addEventListener('click', () => {
        nameInputElement.value = contactInfo.name;
        numberInputElement.value = contactInfo.phone;
        categoryElement.value = contactInfo.category;

        liElement.remove();
      })

      const saveBtnElement = document.createElement('button');
      saveBtnElement.classList.add('save-btn');
      divButtonstElement.appendChild(saveBtnElement);
      saveBtnElement.addEventListener('click', () => {
        contactListElement.appendChild(liElement);
        divButtonstElement.remove();

        const deleteBtnElement = document.createElement('button');
        deleteBtnElement.classList.add('del-btn');
        liElement.appendChild(deleteBtnElement);
        deleteBtnElement.addEventListener('click', () => {
          liElement.remove();
        });
      });
      
      liElement.appendChild(articleElement);
      liElement.appendChild(divButtonstElement);

      return liElement;
    }

    function clearInputFields () {
      nameInputElement.value = '';
      numberInputElement.value = '';
      categoryElement.value = '';
    }
  }
  