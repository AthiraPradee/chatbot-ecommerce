async function askBot() {
  const input = document.getElementById("userInput").value;
  let url = "";

  if (input.includes("top")) {
    url = "/top-products";
  } else if (input.includes("order")) {
    const id = input.match(/\d+/)[0];
    url = `/order-status/${id}`;
  } else if (input.includes("stock")) {
    const item = input.split("stock")[1].trim();
    url = `/stock/${item}`;
  }

  const res = await fetch(url);
  const data = await res.json();
  document.getElementById("response").innerText = JSON.stringify(data, null, 2);
}
