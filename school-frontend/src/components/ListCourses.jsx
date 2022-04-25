import { useEffect, useState } from 'react';

function ListCourses() {
  const [courses, setCourses] = useState([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_BASE_API_URL}/courses`)
      .then((res) => {
        if (!res.ok) {
          // Something went wrong, do whatever you want with it (good luck).
        }

        return res.json();
      })
      .then((data) => setCourses(data))
      .catch((err) => console.error(err))
      .finally(() => setLoaded(true));
  }, []);

  if (!loaded) {
    return <h1>Carregando...</h1>;
  }

  return (
    <>
      {courses.map((course) => {
        return (
          <h2 key={course.id} className="App-table">
            {course.description}
          </h2>
        );
      })}
    </>
  );
}

export default ListCourses;
