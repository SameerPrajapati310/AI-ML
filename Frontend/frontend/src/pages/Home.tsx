import { useState } from 'react'
import './home.css'

function App() {
  const [row, setrow] = useState('0')
  const [col, setcol] = useState('0')
  const [matrix, setmatrix] = useState([])
  const [adj, setadj] = useState({})

  const setmatrixvalues = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/matrix', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          row: Number(row),
          col: Number(col)
        })
      })

      const data = await response.json()

      setmatrix(data.matrix)
    } catch (error) {
      console.log('Error:', error)
    }
  }

  const setrowval = (event) => {
    setrow(event.target.value)
  }

  const setcolval = (event) => {
    setcol(event.target.value)
  }

  const handleMatrixChange = async (rowIndex, colIndex, value) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/matrix/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          rowIndex: rowIndex,
          colIndex: colIndex,
          value: Number(value)
        })
      })

      const data = await response.json()

      setmatrix(data.matrix)
    } catch (error) {
      console.log('Error:', error)
    }
  }

  const createadjlist = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/adj', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      })

      const data = await response.json()

      setadj(data.adj)
    } catch (error) {
      console.log('Error:', error)
    }
  }

  return (
    <div className="container">
      <div className="title">Matrix creation</div>

      <div className="input-section">
        <input
          type="text"
          value={row}
          onChange={setrowval}
          placeholder="Rows"
        />

        <input
          type="text"
          value={col}
          onChange={setcolval}
          placeholder="Columns"
        />
      </div>

      <button className="create-button" onClick={setmatrixvalues}>
        Create Matrix
      </button>

      <div className="matrix-container">
        {matrix.map((rows, rowsindex) => {
          return (
            <div className="matrix-row" key={rowsindex}>
              {rows.map((cols, colindex) => {
                return (
                  <input
                    key={colindex}
                    className="matrix-input"
                    type="text"
                    value={cols}
                    onChange={(event) =>
                      handleMatrixChange(
                        rowsindex,
                        colindex,
                        event.target.value
                      )
                    }
                  />
                )
              })}
            </div>
          )
        })}
      </div>

      <button className="adj-button" onClick={createadjlist}>
        Create Adjacency List
      </button>

      <div className="graph-container">
        <h2>Adjacency List</h2>

        {Object.entries(adj).map(([node, neighbors]) => {
          return (
            <div key={node} className="graph-node">
              <div className="node-circle">{node}</div>

              <div className="neighbor-list">
                {neighbors.length > 0 ? (
                  neighbors.map((neighbor, index) => {
                    return (
                      <div key={index} className="neighbor-circle">
                        {neighbor}
                      </div>
                    )
                  })
                ) : (
                  <div className="no-neighbor">No edges</div>
                )}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default App