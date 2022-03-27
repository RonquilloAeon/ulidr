use pyo3::prelude::*;
use rusty_ulid::generate_ulid_bytes;

#[pyfunction]
fn generate_ulid() -> [u8; 16] {
    generate_ulid_bytes()
}

#[pymodule]
fn _rust_ulid(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_ulid, m)?)?;
    Ok(())
}
