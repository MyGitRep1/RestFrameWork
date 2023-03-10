import React from 'react'


const BookItem = ({item}) => {
     return (
          <tr>
              <td>
                  {item.id}
               </td>
               <td>
                   {item.name}
               </td>
               <td>
                   {item.author.first_name}
               </td>
          </tr>
     )
}


const BookList = ({author}) => {
     return (
        <table>
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Author
            </th>
            {item.map(item) => <BookItem item={item} />)}
        </table>
     )
}


export default BookList;