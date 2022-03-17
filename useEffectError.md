I realized that useEffect does not immediately capture the state in redux

So I added an event listener - which listens to the submission button to reload state after submission is done.

```js

export const Meeting = () => {
    // ...Code and code...
    const [effect, setEffect] = useState(0);
    const newEffect = effect + 1
    
    useEffect(()=>{
        dispatch(getJournal('meeting'))
    }, [dispatch, effect])
}

// on the return, the button is as below:
return (
    <div>
    {/*some more code*/}
    <Button onClick={()=>{
        // More and more code
        setEffect(newEffect)
    }}>
    </div>
)
```
After submission, the button action triggers setEffect function, and causes a change in the effect value. Then the useEffect function listens to the effect value change, and thus is forced to run. 
It is just a work around.


Although I still have a problem:
    That even if the promise is not fulfilled, the alert box returns true