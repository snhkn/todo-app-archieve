package com.github.snhkn.rest.webservices.todoAppwebservice.todo;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.stereotype.Service;

@Service
public class TodoHardcodedService {

	private static List<Todo> todos = new ArrayList();
	private static long idCounter = 0;

	static {
		todos.add(new Todo(++idCounter, "defaultuser", "Learn Angular", new Date(), false, 0));
		todos.add(new Todo(++idCounter, "defaultuser", "Clean the house", new Date(), false, 0));
		todos.add(new Todo(++idCounter, "defaultuser", "Study German", new Date(), false, 0));
		todos.add(new Todo(++idCounter, "defaultuser", "Go shopping", new Date(), false, 0));
	}

	public List<Todo> findAll() {
		return todos;
	}

	public Todo save(Todo todo) {
		if (todo.getId() == -1 || todo.getId() == 0) {
			todo.setId(++idCounter);
			todos.add(todo);
		} else {
			deleteById(todo.getId());
			todos.add(todo);
		}
		return todo;
	}

	public Todo deleteById(long id) {
		Todo todo = findById(id);

		if (todo == null)
			return null;

		if (todos.remove(todo)) {
			return todo;
		}

		return null;
	}

	public Todo findById(long id) {
		for (Todo todo : todos) {
			if (todo.getId() == id) {
				return todo;
			}
		}
		return null;
	}
}
