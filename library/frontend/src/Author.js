import React from 'react'


const AuthorItem = ({author}) => {
     return (
          <tr>
              <td>
                  {author.id}
               </td>
               <td>
                   {author.first_name}
               </td>
               <td>
                   {author.birtday_year}
               </td>
          </tr>
     )
}


const AuthorList = ({author}) => {
     return (
        <table>
            <th>
                ID
            </th>
            <th>
                First name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map(author) => <AuthorItem author={author} />)}
        </table>
     )
}


export default AuthorList