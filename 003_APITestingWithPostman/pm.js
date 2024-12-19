pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response has token", function () {
  pm.expect(pm.response.json()).to.have.property("token");
});
