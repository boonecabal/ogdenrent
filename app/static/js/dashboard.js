document.addEventListener('DOMContentLoaded', () => {
  const deleteButtons = document.querySelectorAll('button.delete_button');
  deleteButtons.forEach((button) => {
    button.addEventListener('click', () => {
      onDelete(button.id);
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const deleteButtons = document.querySelectorAll('button.camera_button');
  deleteButtons.forEach((button) => {
    button.addEventListener('click', () => {
      onCamera(button.id);
    });
  });
});

function onDelete(id) {
  const numericString = id.match(/\d+$/)[0];
  const numericId = parseInt(numericString);

  fetch(`delete_customer/${numericId}`, {
    method: 'DELETE',
  })
  .then(response => {
    window.location.reload();
  })
  .catch(error => {
    console.log(error);
  });

}

function onCamera(id) {
  const numericString = id.match(/\d+$/)[0];
  const numericId = parseInt(numericString);

  const username = 'boone.cabal@gmail.com';
  const password = 'grantaster';
  const encoded = btoa(`${username}:${password}`);
  const the_url = `http://127.0.0.1:5000/active_customer/${numericId}`;

  fetch(the_url, {
    method: 'PUT',
  })
  .then(response => {
    if (response.ok)
      LaunchURLScript();
  })
  .catch(error => {
    console.log(error);
  });

}

function LaunchURLScript() {
  var url = "CypherionProtocol:";
  window.open(url);
  self.focus();
}

/*
function onCamera(id) {
  const numericString = id.match(/\d+$/)[0];
  const numericId = parseInt(numericString);

  const username = 'boone.cabal@gmail.com';
  const password = 'grantaster';
  const encoded = btoa(`${username}:${password}`);
  const the_url = `http://127.0.0.1:5000/api/v1/active_customer/${numericId}`;

  $.ajax({
    url: the_url,
    type: 'PUT',
    headers: {
      'Authorization': `Basic $(encoded)`,
    },
    xhrFields: {
      withCredentials: true
    },
    success: function(response) {
      console.log(`Customer with id ${numericId} was made the active Customer, fiend.`);
      //location.reload();
    },
    error: function(xhr, status, error) {
      console.error(`Error: ${error}`);
    }
  });
}
*/