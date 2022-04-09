use pyo3::prelude::*;
use rusty_ulid::generate_ulid_string;

#[pyfunction]
fn generate_ulid() -> String {
    generate_ulid_string()
}

#[pymodule]
fn _rust_ulid(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_ulid, m)?)?;
    Ok(())
}
